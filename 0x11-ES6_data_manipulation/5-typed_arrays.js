function createInt8TypedArray(length, position, value) {
  if (position >= length || position < 0) throw Error('Position outside range');

  const arr = new Int8Array(length);
  arr[position] = value;

  return new DataView(arr.buffer, 0, length);
}

export default createInt8TypedArray;
