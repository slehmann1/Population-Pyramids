YEAR_I = 2001;
YEAR_F = 2020;
year_array = Array.from({ length: YEAR_F - YEAR_I + 1 }, (x, i) => i + YEAR_I);
curr_i = 0;
DELAY = 1000;
yearLabel = []

plot_loop();

async function plot_loop() {
    const { maleChart, femaleChart, data } = genChart()
    while (true) {
        updateChart(data, maleChart, femaleChart, year_array[curr_i]);
        curr_i++;
        if (curr_i >= year_array.length) {
            curr_i = 0;
        }
        await new Promise(resolve => setTimeout(resolve, DELAY));
    }
}

function genChart() {
    console.log("GENERATING CHART")
    year = year_array[0]

    data = JSON.parse(
        document.currentScript.nextElementSibling.textContent
    );

    yearLabel = document.getElementById('yearLabel')
    yearLabel.innerHTML = String(year)

    ctx = document.getElementById('males');

    maleChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data[year]["age"],
            datasets: [{
                label: 'Male',
                data: data[year]["male"],
                borderWidth: 1,
                borderColor: '#36A2EB',
                backgroundColor: '#36A2EB',
            },]
        },
        options: {
            indexAxis: "y",
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Age",
                        position: "right"
                    },
                    reverse: true,
                    position: "right"
                },
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Count"
                    },
                    afterFit: (axis) => {
                        axis.paddingLeft = 0;
                    },
                    max: data["max_count"]
                }
            },
            layout: {
                padding: {
                    left: 0
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: "Male"
                },
                legend:{
                    display:false
                }
            }
        }
    });

    ctx = document.getElementById('females');

    femaleChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data[year]["age"],
            datasets: [{
                label: 'Female',
                data: data[year]["female"],
                borderWidth: 1,
                borderColor: '#ff8cdb',
                backgroundColor: '#ff8cdb',
            }]
        },
        options: {
            indexAxis: "y",
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Age"
                    },
                    reverse: true,
                },
                x: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: "Count"
                    },
                    reverse: true,
                    afterFit: (axis) => {
                        axis.paddingRight = 0;
                    },
                    max: data["max_count"]
                }
            },
            layout: {
                padding: {
                    right: 0
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: "Female"
                },
                legend:{
                    display:false
                }
            }

        }
    });

    return { maleChart: maleChart, femaleChart: femaleChart, data: data }

}



function updateChart(data, maleChart, femaleChart, year) {
    console.log("Year " + year)
    console.log(data)

    maleChart.data.datasets[0].data = data[year]["male"]
    maleChart.data.labels = data[year]["age"]
    maleChart.update()

    femaleChart.data.datasets[0].data = data[year]["female"]
    femaleChart.data.labels = data[year]["age"]
    femaleChart.update()

    yearLabel.innerHTML = String(year)

}