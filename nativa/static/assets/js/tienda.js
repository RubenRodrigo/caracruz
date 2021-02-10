const filtros = document.querySelector(".filtros")
const productos = document.querySelector(".productos")
//const catalogos = document.querySelector(".hero-tienda")
var body = document.body

eventListener()
function eventListener() {
    filtros.addEventListener('click', mostraFiltros)
    productos.addEventListener('click', mostrarProducto)
    productos.addEventListener('mouseover', cambiarImagen)
    productos.addEventListener('mouseout', volverImagen)
}
function mostraFiltros(e) {
    if (e.target.classList.contains("catalogo")) {
        const categoria = e.target.nextElementSibling
        if (categoria.classList.contains('options-active')) {
            categoria.classList.remove("options-active")
        } else {
            categoria.classList.add("options-active")
        }
    }
    if (e.target.classList.contains("catalogo-img")) {
        const categoria = e.target.parentElement.nextElementSibling
        if (categoria.classList.contains('options-active')) {
            categoria.classList.remove("options-active")
        } else {
            categoria.classList.add("options-active")
        }
    }
}

function mostrarProducto(e) {    
    if (e.target.classList.contains("ver-producto")) {
        e.preventDefault()
        const verProducto = e.target
        var modal = verProducto.parentElement.parentElement.nextElementSibling            
        body.style.overflow = 'hidden'
        modal.classList.add('modal-box-active')
        modal.addEventListener('click', funcionalidadModal)
        window.onclick = function(e) {
            if (e.target == modal) {
                modal.classList.remove('modal-box-active')
                body.style.overflow = 'scroll'
                e.preventDefault()
            }
        }
    }
    if (e.target.classList.contains("ver-producto-span")) {
        e.preventDefault()
        const verProducto = e.target.parentElement
        var modal = verProducto.parentElement.parentElement.nextElementSibling            
        body.style.overflow = 'hidden'
        modal.classList.add('modal-box-active')
        modal.addEventListener('click', funcionalidadModal)
        window.onclick = function(e) {
            if (e.target == modal) {
                modal.classList.remove('modal-box-active')
                body.style.overflow = 'scroll'
                e.preventDefault()
            }
        }
    }
}

function funcionalidadModal(e) {
    if(e.target.classList.contains("close")){
        body.style.overflow = 'scroll'
        e.preventDefault()
        var modal = e.target.parentElement.parentElement
        modal.classList.remove('modal-box-active')
    }
}

function cambiarImagen(e) {
    console.log(e);
    if(e.target.classList.contains("producto-imagen")){            
        var imagen = e.target
        imagen.src = imagen.dataset.productosecond;            
    }
}

function volverImagen(e) {
    console.log(e);
    if(e.target.classList.contains("producto-imagen")){
        var imagen = e.target
        imagen.src = imagen.dataset.productofirst;
    }
}