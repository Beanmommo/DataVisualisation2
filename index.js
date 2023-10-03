var map = "salesMapData.vg.json";
var factoryMap = "factoryMapData.vg.json";
var salesProdBarGraph = "salesProductionGraphs.vg.json"
vegaEmbed('#factory-location-map', factoryMap).then(function(result) {
    // Access vega view
}).catch(console.error);
vegaEmbed('#prod-sales-graph', salesProdBarGraph).then(function(result) {

}).catch(console.error);