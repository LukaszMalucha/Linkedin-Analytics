import { Bar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: Bar,
  mixins: [reactiveProp],
  data(){
    return {
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          xAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                fontSize: 10
              }
          }],
          yAxes: [{
              gridLines: {
                  color: "rgba(0, 0, 0, 0)",
              },
              ticks: {
                stepSize: 20
              }
          }],

        },
        legend: {
          display: false
        },
        tooltips: {
          enabled: true,
          callbacks: {
            label: function(tooltipItem,data) {
              return data['datasets'][0]['data'][tooltipItem['index']] + " companies";
            },
          }
        }
      }
    }
  },
  mounted () {
    this.renderChart(
      this.chartData,
      this.options
      )
  }
}
