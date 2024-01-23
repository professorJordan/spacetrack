const map = L.map('map', {
    center: [-29.50, 145],
    zoom: 3.5
  });
  
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);
  
  

  const marker1 = L.marker([10.79798253965187, 169.1551358849787]).addTo(map);
  const marker2 = L.marker([9.7550, 168.9178]).addTo(map);
  const marker3 = L.marker([-30.1576, 159.5355]).addTo(map);
  const marker4 = L.marker([-38.3085, 157.1260]).addTo(map);