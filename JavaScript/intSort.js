function descendingOrder(n){
  //first I can convert the Integer to a String and organise it that way, then convert it back.
  const stringSort = n.toString().split('').sort((a,b) => b-a).join('');
  const result = parseInt(stringSort, 10)
  
  return result;
}
