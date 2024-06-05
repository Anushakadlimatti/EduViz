const labels = {{labels| tojson}};
const data ={labels: labels,datasets:{{datasets | tojson}}};
console.log(data);

const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Floating Bar Chart'
      }
    }
  }
};
//// Create a new chart instance
//var ctx = document.getElementById('myChart').getContext('2d');
//var myChart = new Chart(ctx, config);