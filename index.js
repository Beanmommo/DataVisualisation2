var map = "salesMapData.vg.json";
var factoryMap = "factoryMapData.vg.json";
vegaEmbed('#map', map).then(function(result) {
    // Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);
vegaEmbed('#factory-location-map', factoryMap).then(function(result) {
    // Access vega view
}).catch(console.error);