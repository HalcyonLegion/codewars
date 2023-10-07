// return masked string of any length greater than or equal to 4 and masks the final 4 digits.
function maskify(cc) {
  if (cc.length <= 4) {
    return cc;
  }
  
  const lastFour = cc.slice(-4);
  
  const masking = '#'.repeat(cc.length - 4);
  
  return masking + lastFour;
}
