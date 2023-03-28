function cleanSet(set, startString) {
  const resultArr = [];

  if (!startString || !startString.length) return '';

  for (const word of set) {
    if (word && word.startsWith(startString)) {
      resultArr.push(word.slice(startString.length));
    }
  }

  return resultArr.join('-');
}

export default cleanSet;
