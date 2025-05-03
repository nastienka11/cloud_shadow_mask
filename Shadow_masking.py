2)Clouds shadow

//VERSION=3

 function RGBToColor (r, g, b,dataMask){
  return [r/255, g/255, b/255,dataMask];
}

function setup() {
   return {
    input: ["SCL","dataMask"],
    output: { bands: 1 }
  };
}

function evaluatePixel(samples) {
    const SCL = samples.SCL;
    switch (SCL) {
      // Cloud shadows (dark brown)
      case 3: return RGBToColor(100, 50, 0, samples.dataMask);
      // No data (values that are not cloud shadows)
      default: return [-999999999.000000];
    }
}
