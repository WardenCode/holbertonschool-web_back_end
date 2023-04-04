class AppController {
  static getHomepage(request, response) {
    response.status(200).send('Hello Holberton School!\n');
  }
}

export default AppController;
