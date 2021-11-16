var toon = "https://looney-toons-api.herokuapp.com/api/characters"
 
async function getToon() {
   var response = await fetch(`${toon}`)
   var data = await response.json()
   console.log("full api data", data)
   console.log("narrowing it down", data.data)
//    console.log("showing 1 index", data.data[10])
    var node = document.createElement('div')
    
//    var result = document.getElementById('toon')
   for (var i = 0; i < data.data.length; i++) {
       console.log(data.data[i])
       var img = new Image()
       img.src = `${data.data[i].img}`
       img.alt = `${data.data[i].name}`
       node.appendChild(img)
   }
   document.getElementById('toon').appendChild(node)
}
function search(e){
    e.preventDefault();
    var searchForm = document.getElementById('searchForm')
    var form = new FormData(searchForm);
    fetch('http://localhost:5000/search',{method:'GET',body:form})
        .then(res => res.json() )
        .then( data => console.log(data) )
        .catch(err => console.log(err))
}