// make line chart
export function footprintPlot(plotLabels, plotData) {
    let ctx = document.getElementById("footprintPlot").getContext("2d");
    let footprintPlot = new Chart(ctx, {
        type: "line",
        data: {
            datasets: [
                {
                    label: "Your Carbon Footprint (kilograms)",
                    data: plotData,
                    // set options for the chart
                    backgroundColor: ["rgba(255, 99, 132, 0.2)"],
                    borderColor: ["rgba(255, 99, 132, 1)"],
                    borderWidth: 1,
                },
            ],
            labels: plotLabels,
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [{
                    display: true,
                    ticks: {
                        max: 20000,
                        beginAtZero: true,
                        // turn the tick markers white
                        fontColor: 'rgb(255, 255, 255)'
                    },
                    gridLines: {
                        color: "white",
                        display: true
                    }
                }],
                yAxes: [{
                    ticks: {
                        // color the plot label white
                        fontColor: "white",
                        label: "Your Footprint (kilograms)"
                    },
                    // add white lines going parallel to the x-axis
                    gridLines: {
                        color: "white",
                        display: true
                    }
                }],
            },
            // turn the legend white
            legend: {
                display: true,
                labels: {
                    fontColor: 'rgb(255, 255, 255)',
                }
            },
        },
    });
}
