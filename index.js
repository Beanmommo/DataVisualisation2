var map = "salesMapData.vg.json";
var factoryMap = "factoryMapData.vg.json";
var salesProdBarGraph = "salesProductionGraphs.vg.json"
var top10car = "top10CarGraph.vg.json"
var marketCapLineGraph = "marketCapLineGraph.vg.json"
var marketCap2023BarGraph = "marketCap2023Graph.vg.json"
vegaEmbed('#factory-location-map', factoryMap).then(function(result) {
    // Access vega view
}).catch(console.error);
vegaEmbed('#prod-sales-graph', salesProdBarGraph).then(function(result) {

}).catch(console.error);
vegaEmbed('#top10car', top10car).then(function(result) {

}).catch(console.error);
vegaEmbed('#top10market', marketCapLineGraph).then(function(result) {

}).catch(console.error);
vegaEmbed('#top10autocompany', marketCap2023BarGraph).then(function(result) {

}).catch(console.error);