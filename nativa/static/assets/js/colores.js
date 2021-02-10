var productosColor = document.querySelectorAll('.producto-container')

eventListenerColores()
function eventListenerColores(){			
	productosColor.forEach((producto) => {
		var colores = producto.querySelector('.producto-colores')
		colores.addEventListener('click', mostrarColor)
		var tallas = producto.querySelector('.producto-tallas')
		tallas.addEventListener('click', mostrarTalla)
	})			
}
function mostrarColor(e){
	var colores = this
	if(e.target.classList.contains('color')){				
		var coloresInactivos = colores.querySelectorAll(".colores--prenda")
		coloresInactivos.forEach(element => {
			element.id = ""
		});
		var color = e.target
		color.parentElement.id = "active"				
	}
}
function mostrarTalla(e){
	var tallas = this
	if(e.target.classList.contains('talla')){				
		var tallasInactivos = tallas.querySelectorAll(".talla")
		tallasInactivos.forEach(element => {
			element.classList.remove("active")
		});
		var talla = e.target
		talla.classList.add("active")		
	}
}