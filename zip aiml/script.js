gsap.to(".navbar",{
       backgroundColor : "#000",
       duration: 1,
       height : "60px",
       scrollTrigger : {
        trigger : ".navbar",
        scroller : "body",
        start: "top -10%",  
        end: "top -11%",
        scrub: 1
       }

})

