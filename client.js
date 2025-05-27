(function(){
  // html2canvas yuklaymiz
  var s = document.createElement('script');
  s.src = 'https://html2canvas.hertzen.com/dist/html2canvas.min.js';
  s.onload = function(){
      startAutoCapture();
  };
  document.head.appendChild(s);

  function startAutoCapture(){
    const ws = new WebSocket("ws://localhost:8080");

    ws.onopen = function(){
      console.log("✅ WebSocket ulanishi ochildi");

      setInterval(function(){
        html2canvas(document.body).then(function(canvas){
          const dataURL = canvas.toDataURL("image/png");
          ws.send(dataURL);
          console.log("📤 Skrinshot yuborildi");
        });
      }, 3000); // har 3 soniyada
    };

    ws.onclose = function(){
      console.log("❌ WebSocket ulanmasi uzildi");
    };
  }
})();
