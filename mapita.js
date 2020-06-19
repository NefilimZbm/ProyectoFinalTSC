
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
		'f': 2,
		'vecinos': 'El Nigromante, Minatitlán  y San Andrés Tuxtla.',
		'icon': creaIcono( 'images/acayucan.png', 18, 31)
	},
	'alvarado': {
		'titulo': 'Alvarado',
		'coordenadas': [18.76961, -95.75894],
		'f': 2,
		'vecinos': 'Boca del Rio, Otatitlán y San Andrés Tuxtla.',
		'icon': creaIcono( 'images/alvarado.png', 18, 31)
	},
	'boca': {
		'titulo': 'Boca Del Rio',
		'coordenadas': [19.10627, -96.10632],
		'f': 2,
		'vecinos': 'Alvarado, Joachín, Xalapa y Zempoala.',
		'icon': creaIcono('images/bocadelrio.png', 18, 31)
	},
	'coatzacoalcos': {
		'titulo': 'Coatzacoalcos',
		'coordenadas': [18.13447, -94.45898],
		'f': 2,
		'vecinos': 'Agua Dulce, Minatitlán y San Andrés Tuxtla.',
		'icon': creaIcono('images/coatza.png', 18, 31)
	},
	'aguadulce': {
		'titulo': 'Agua Dulce',
		'coordenadas': [18.14259, -94.1436],
		'f': 1,
		'vecinos': 'Coatzacoalcos.',
		'icon': creaIcono('images/aguadulce.png', 18, 31)
	},
	'huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314],
		'f': 2,
		'vecinos': 'Fortín de las Flores y Otatitlán.',
		'icon': creaIcono('images/huautla.png', 18, 31)
	},
	'fortin': {
		'titulo': 'Fortín de las Flores',
		'coordenadas': [18.9017, -96.99896],
		'f': 2,
		'vecinos': 'Huatusco y Yanga.',
		'icon': creaIcono('images/fortin.png', 18, 31)
	},
	'huatusco': {
		'titulo': 'Huatusco',
		'coordenadas': [19.14823, -96.96654],
		'f': 2,
		'vecinos': 'Fortín de las Flores y Xalapa.',
		'icon': creaIcono('images/huatusco.png', 18, 31)
	},
	'joachin': {
		'titulo': 'Joachín',
		'coordenadas': [18.6407, -96.23095],
		'f': 2,
		'vecinos': 'Boca del Rio, Otatitlán y Yanga.',
		'icon': creaIcono('images/joachin.png', 18, 31)
	
	},
	'minatitlan': {
		'titulo': 'Minatitlán',
		'coordenadas': [17.99392, -94.5466],
		'f': 2,
		'vecinos': 'Acayucan y Coatzacoalcos.',
		'icon': creaIcono('images/minatitlan.png', 18, 31)
	},
	'nigromante': {
		'titulo': 'El Nigromante',
		'coordenadas': [17.76323, -95.75574],
		'f': 2,
		'vecinos': 'Acayucan y Otatitlán.',
		'icon': creaIcono('images/nigromante.png', 18, 31)
	},
	'otatitlan': {
		'titulo': 'Otatitlán',
		'coordenadas': [18.18106, -96.03439],
		'f': 2,
		'vecinos': 'Alvarado, Huautla de Jiménez, Joachín y El Nigromante.',
		'icon': creaIcono('images/otatitlan.png', 18, 31)
	},
	'papantla': {
		'titulo': 'Papantla',
		'coordenadas': [20.45667, -97.31561],
		'f': 2,
		'vecinos': 'Tecolutla, Teziutlán y Vega de Alatorre.',
		'icon': creaIcono('images/papantla.png', 18, 31)
	},
	'tecolutla': {
		'titulo': 'Tecolutla',
		'coordenadas': [20.47955, -97.01012],
		'f': 2,
		'vecinos': 'Papantla y Vega de Alatorre.',
		'icon': creaIcono('images/tecolutla.png', 18, 31)
	},
	'teziutlan': {
		'titulo': 'Teziutlán',
		'coordenadas': [19.81601, -97.35705],
		'f': 2,
		'vecinos': 'Papantla y Xalapa.',
		'icon': creaIcono('images/teziutlan.png', 18, 31)
	},
	'sanandres': {
		'titulo': 'San Andrés Tuxtla',
		'coordenadas': [18.44412, -95.21302],
		'f': 2,
		'vecinos': 'Acayucan, Alvarado y Coatzacoalcos.',
		'icon': creaIcono('images/tuxtla.png', 18, 31)
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044],
		'f': 2,
		'vecinos': 'Papantla, Tecolutla, Xalapa y Zempoala.',
		'icon': creaIcono('images/vega.png', 18, 31)
	},
	'xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		'f': 2,
		'vecinos': 'Boca del Rio, Huatusco, Teziutlán, Vega de Alatorre y Zempoala.',
		'icon': creaIcono('images/xalapa.png', 18, 31)
	},
	'yanga': {
		'titulo': 'Yanga',
		'coordenadas': [18.82928, -96.80027],
		'f': 2,
		'vecinos': 'Fortín de las Flores y Joachín.',
		'icon': creaIcono('images/yanga.png', 18, 31)
	},
	'zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507],
		'f': 2,
		'vecinos': 'Boca del Rio, Vega de Alatorre y Xalapa.',
		'icon': creaIcono('images/zempoala.png', 18, 31)
	}
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	//console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
		if (item[1].f===1) {
			marker.bindPopup(`<b>Soy ${item[1].titulo}</b><br>Mis coordenadas son (${item[1].coordenadas})<br>Mi vecino es ${item[1].vecinos}`);
		} else {
			marker.bindPopup(`<b>Soy ${item[1].titulo}</b><br>Mis coordenadas son (${item[1].coordenadas})<br>Mis vecinos son ${item[1].vecinos}`);
		}
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}

}
window.onload = function(){
	document.getElementById("boton").addEventListener("click",cambia);
}
function cambia(){
	var partida = document.getElementById("org").value;
	var llegada = document.getElementById("lle").value;
	var flag = new Boolean(false);
	var m = new Map();
	primer = {};
	vecinos = [];
	if(partida == llegada){
    		alert("El origen y destino es lo mismo");
	}else{
		var d_tan = mymap.distance(locations.partida.coordenadas, locations.llegada.coordenadas);
		m.set(partida,d_tan);
		recorrido = [];
		/*
		while(m.length != 0){
			primero[partida]=d_tan;
			
		}*/
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
var polyline = L.polyline(ruta1, {color: 'teal'}).addTo(mymap);

console.log(mymap.distance(locations.xalapa.coordenadas, locations.zempoala.coordenadas) + ' metros');







