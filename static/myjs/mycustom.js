$('#recipeCarousel').carousel({
  interval: 10000
})

$('.carousel .carousel-item').each(function(){
    var minPerSlide = 3;
    var next = $(this).next();
    if (!next.length) {
    next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    for (var i=0;i<minPerSlide;i++) {
        next=next.next();
        if (!next.length) {
        	next = $(this).siblings(':first');
      	}

        next.children(':first-child').clone().appendTo($(this));
      }
});


let accordions = document.querySelectorAll('.accordion')
accordions.forEach(accordion => {
    console.log(accordion.children)
    Array.from(accordion.children).forEach(wrapper => {
        if (wrapper.classList.contains('show')) {
            wrapper.querySelector('div').style.maxHeight = wrapper.scrollHeight + 30 + 'px'
        }
        wrapper.querySelector('span').addEventListener('click', e => {
            console.log(e.target)
            let span = e.target
            let wrapper = span.parentElement
            let div = span.nextElementSibling
            wrapper.classList.toggle('show')
            console.log(div.scrollHeight)
            if (wrapper.classList.contains('show')) {
                div.style.maxHeight = div.scrollHeight +30 + "px"
            } else {
                div.style.maxHeight = null
            }
            Array.from(accordion.children).forEach(w => {
                if (w != wrapper) {
                    w.classList.remove('show')
                    w.querySelector('div').style.maxHeight = null
                }
            })
        })
    })
})

