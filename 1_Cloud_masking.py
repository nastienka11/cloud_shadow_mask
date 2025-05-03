
1)Clouds

function setup() {
  return {
    input: ["B02", "B03", "B04", "CLM"],
    output: { bands: 1 }
  }
}

function evaluatePixel(sample) {
  if (sample.CLM == 1) {
    return [0.75 + sample.B04];
  } else {
    return [null];
  }
}

