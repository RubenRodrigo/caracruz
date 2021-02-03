var artesanos = document.querySelector('.artesano-container')

eventListeners()
function eventListeners(){
    window.addEventListener('scroll', scrollAppear)
    artesanos.addEventListener('click', verMas)
}
function scrollAppear(){
    var artesano_par = document.querySelector('.artesano-par')
    var artesano_impar = document.querySelector('.artesano-impar')
    var introPosition_par = artesano_par.getBoundingClientRect().top
    var introPosition_impar = artesano_impar.getBoundingClientRect().top
    var screenPosition = window.innerHeight / 2
    if(introPosition_par < screenPosition){
        artesano_par.querySelector('.image').classList.add('active')
    }
    if(introPosition_impar < screenPosition){
        artesano_impar.querySelector('.image').classList.add('active')
    }
}
function verMas(e) {
    if(e.target.classList.contains('ver-mas')){
        var button = e.target
        var video_box = button.parentElement.parentElement.parentElement.parentElement.nextElementSibling
        var video = video_box.querySelector('#myVideo')
        console.log(button);
        if (video_box.classList.contains('artesano-video-active')){
            video_box.classList.remove('artesano-video-active')
            button.innerHTML = "Saber mas"
            video.pause()
        } else {
            video_box.classList.add('artesano-video-active')
            button.innerHTML = "Ocultar"
            video.play()
        }

    }
}