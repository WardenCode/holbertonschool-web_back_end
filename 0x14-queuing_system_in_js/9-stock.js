import express from 'express';
import redis from 'redis'
import { promisify } from 'util';

const port = 1245;
const hostname = 'localhost';
const app = express();

const client = redis.createClient();

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2
    },
    {
        id: 4 ,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    },
];

const getItemById = id => {
    const itemId = Number(id);
    if (isNaN(itemId)) return undefined;

    return listProducts.find(product => product.id === itemId);
};

const productResFormat = ({ id, name, price, stock }) => ({
    itemId: id,
    itemName: name,
    price: price,
    initialAvailableQuantity: stock,
});

const getAsync = promisify(client.get).bind(client);

const getCurrentReservedStockById = async itemId => {
    let reservedStock = parseInt(await getAsync(`item.${itemId}`));

    if (isNaN(reservedStock)) return undefined;

    return reservedStock;
};

const reserveStockById = (itemId, reservedStock) => {
    client.set(`item.${itemId}`, reservedStock ? reservedStock + 1 : 1);
}

client.on('connect', () => console.log(`Redis client connected to http://localhost:${port}`));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

app.get('/list_products', (req, res) => {
    return res.json(listProducts.map(item => productResFormat(item)));
});

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
    const { itemId } = req.params;
    const item = getItemById(itemId);

    if (!item) return res.status(404).json({ status: 'Product not found' });

    const reservedStock = await getCurrentReservedStockById(itemId);

    const productInfo = {
      ...productResFormat(item),
      currentQuantity: item.stock - reservedStock,
    };

    return res.json(productInfo);
});

app.get('/reserve_product/:itemId(\\d+)', async (req, res) => {
    const { itemId } = req.params;
    const item = getItemById(itemId);

    if (!item) {
      return res.status(404).json({ status: 'Product not found' });
    }

    const { stock, id } = item;

    const reservedStock = await getCurrentReservedStockById(itemId);

    if (reservedStock >= stock) {
      return res.status(404).json({ status: 'Not enough stock available', itemId: id });
    }

    reserveStockById(id, reservedStock);

    return res.json({ status: 'Reservation confirmed', itemId: id });
});

app.listen(port, hostname, () => {
    console.log(`app listen in port: ${port}`);
});
