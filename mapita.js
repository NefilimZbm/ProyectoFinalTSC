
var mymap = L.map('mapid').setView([19.046250, -96.259722], 7);

var apiKey = 'pk.eyJ1IjoibmVmaWxpbXpibSIsImEiOiJja2F4MWFxa3gwMjgyMnJubGhndjA2eDM0In0.53G54HQez5adkwvDdGCi5A'

L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${apiKey}`, {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox/streets-v11',
	tileSize: 512,
	zoomOffset: -1
}).addTo(mymap);




function creaIcono(ruta, width, height) {
	var icono = L.icon({
		iconUrl: ruta,
		iconSize: [width, height], 
	});
	return icono;
}

var locations = {
	'acayucan': {
		'titulo': 'Acayucan',
		'coordenadas': [17.94919, -94.91459],
		'icon': creaIcono('images/acayucan.png', 18, 31)
	},
	'alvarado': {
		'titulo': 'Alvarado',
		'coordenadas': [18.76961, -95.75894],
		'icon': creaIcono( 'images/alvarado.png', 18, 31)
	},
	'boca': {
		'titulo': 'Boca Del Rio',
		'coordenadas': [19.10627, -96.10632],
		'icon': creaIcono('images/bocadelrio.png', 18, 31)
	},
	'coatzacoalcos': {
		'titulo': 'Coatzacoalcos',
		'coordenadas': [18.13447, -94.45898],
		'icon': creaIcono('images/coatza.png', 18, 31)
	},
	'aguadulce': {
		'titulo': 'Agua Dulce',
		'coordenadas': [18.14259, -94.1436],
		'icon': creaIcono('images/aguadulce.png', 18, 31)
	},
	'huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314],
		'icon': creaIcono('images/huautla.png', 18, 31)
	},
	'fortin': {
		'titulo': 'Fortín de las Flores',
		'coordenadas': [18.9017, -96.99896],
		'icon': creaIcono('images/fortin.png', 18, 31)
	},
	'huatusco': {
		'titulo': 'Huatusco',
		'coordenadas': [19.14823, -96.96654],
		'icon': creaIcono('images/huatusco.png', 18, 31)
	},
	'joachin': {
		'titulo': 'Joachín',
		'coordenadas': [18.6407, -96.23095],
		'icon': creaIcono('images/joachin.png', 18, 31)
	
	},
	'minatitlan': {
		'titulo': 'Minatitlán',
		'coordenadas': [17.99392, -94.5466],
		'icon': creaIcono('images/minatitlan.png', 18, 31)
	},
	'nigromante': {
		'titulo': 'El Nigromante',
		'coordenadas': [17.76323, -95.75574],
		'icon': creaIcono('images/nigromante.png', 18, 31)
	},
	'otatitlan': {
		'titulo': 'Otatitlán',
		'coordenadas': [18.18106, -96.03439],
		'icon': creaIcono('images/otatitlan.png', 18, 31)
	},
	'papantla': {
		'titulo': 'Papantla',
		'coordenadas': [20.45667, -97.31561],
		'icon': creaIcono('images/papantla.png', 18, 31)
	},
	'tecolutla': {
		'titulo': 'Tecolutla',
		'coordenadas': [20.47955, -97.01012],
		'icon': creaIcono('images/tecolutla.png', 18, 31)
	},
	'teziutlan': {
		'titulo': 'Teziutlán',
		'coordenadas': [19.81601, -97.35705],
		'icon': creaIcono('images/teziutlan.png', 18, 31)
	},
	'sanandres': {
		'titulo': 'San Andrés Tuxtla',
		'coordenadas': [18.44412, -95.21302],
		'icon': creaIcono('images/tuxtla.png', 18, 31)
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044],
		'icon': creaIcono('images/vega.png', 18, 31)
	},
	'xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		'icon': creaIcono('images/xalapa.png', 18, 31)
	},
	'yanga': {
		'titulo': 'Yanga',
		'coordenadas': [18.82928, -96.80027],
		'icon': creaIcono('images/yanga.png', 18, 31)
	},
	'zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507],
		'icon': creaIcono('images/zempoala.png', 18, 31)
	}
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	//console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}

}

// create a red polyline from an array of LatLng points
var ruta1 = [
	
	locations.zempoala.coordenadas,
	locations.vega.coordenadas,
	locations.tecolutla.coordenadas,
	locations.papantla.coordenadas,
	locations.teziutlan.coordenadas,
	locations.xalapa.coordenadas,
	locations.huatusco.coordenadas,
	locations.fortin.coordenadas,
	locations.huautla.coordenadas,
	locations.otatitlan.coordenadas,
	locations.nigromante.coordenadas,
	locations.acayucan.coordenadas,
	locations.minatitlan.coordenadas,
	locations.coatzacoalcos.coordenadas,
	locations.aguadulce.coordenadas,
	locations.coatzacoalcos.coordenadas,
	locations.sanandres.coordenadas,
	locations.alvarado.coordenadas,
	locations.boca.coordenadas,
	locations.zempoala.coordenadas,
	locations.xalapa.coordenadas,
	locations.vega.coordenadas,
	locations.papantla.coordenadas,
	locations.teziutlan.coordenadas,
	locations.xalapa.coordenadas,
	locations.boca.coordenadas,
	locations.joachin.coordenadas,
	locations.yanga.coordenadas,
	locations.fortin.coordenadas,
	locations.yanga.coordenadas,
	locations.joachin.coordenadas,
	locations.otatitlan.coordenadas,
	locations.alvarado.coordenadas,
	locations.sanandres.coordenadas,
	locations.acayucan.coordenadas,
];
var polyline = L.polyline(ruta1, {color: 'red'}).addTo(mymap);

console.log(mymap.distance(locations.xalapa.coordenadas, locations.zempoala.coordenadas) + ' metros');
console.log('hola soy Shani');






