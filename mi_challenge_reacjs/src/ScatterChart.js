import React from "react";
import { Scatter } from "react-chartjs-2";

export default function ScatterChart({ data }) {
  // console.log("data .......");
  // console.log(data.most_popular_dropoff_points);
  let mostPopularDropOff = {};
  let mostPopularPickup = {};
  let dropOffData = [];
  let pickupfData = [];
  let dropOffLabel = [];
  let pickupLabel = [];
  if (data.most_popular_dropoff_points) {
    mostPopularDropOff = JSON.parse(data.most_popular_dropoff_points);
    mostPopularPickup = JSON.parse(data.most_popular_pickup_points);
    // console.log(mostPopularDropOff);
    mostPopularPickup.features.forEach(feature => {
      pickupLabel.push(feature.properties.name);
      data = {
        x: feature.geometry.coordinates[0],
        y: feature.geometry.coordinates[1]
      };
      pickupfData.push(data);
    });
    mostPopularDropOff.features.forEach(feature => {
      dropOffLabel.push(feature.properties.name);
      data = {
        x: feature.geometry.coordinates[0],
        y: feature.geometry.coordinates[1]
      };
      dropOffData.push(data);
      // console.log(data);
    });
  }
  // let mostPopularPickup = JSON.parse(data.most_popular_pickup_points)
  // console.log(mostPopularDropOff)
  // console.log(mostPopularPickup)
  // mostPopularPickup.features.forEach(element => {

  //   });
  //   mostPopularDropOff.features.forEach(element => {

  //   });
  // let data1 = [
  //   { x: 13.406305710121323, y: 52.54096873175922 },
  //   { x: 13.4446535030306, y: 52.545381856568476 },
  //   { x: 13.365558432116691, y: 52.53337051722053 },
  //   { x: 13.466694041753325, y: 52.559273663322855 },
  //   { x: 13.42080856393584, y: 52.53317402906312 },
  //   { x: 13.493951208041736, y: 52.541230104140276 },
  //   { x: 13.407925477070265, y: 52.53687031832495 },
  //   { x: 13.348366070903975, y: 52.56227123652007 },
  //   { x: 13.480702976887098, y: 52.55322588554682 },
  //   { x: 13.378158414242595, y: 52.55323771239874 }
  // ];
  let popularPointData = {
    labels: ["Scatter"],
    datasets: [
      {
        label: "Most popular dropoff point",
        fill: true,
        backgroundColor: "#2B1A7D",
        pointBorderColor: "#3E89EC",
        pointBackgroundColor: "#000000",
        pointBorderWidth: 15,
        pointHoverRadius: 15,
        pointHoverBackgroundColor: "rgba(75,192,192,1)",
        pointHoverBorderColor: "rgba(220,220,220,1)",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 10,
        data: dropOffData
      },
      {
        label: "Most popular pickup point",
        fill: true,
        backgroundColor: "#58E55C",
        pointBorderColor: "#58E55C",
        pointBackgroundColor: "#2345678",
        pointBorderWidth: 15,
        pointHoverRadius: 15,
        pointHoverBackgroundColor: "#269729",
        pointHoverBorderColor: "#269729",
        pointHoverBorderWidth: 2,
        pointRadius: 1,
        pointHitRadius: 1,
        data: pickupfData
      }
    ]
  };

  const options = { 
    options: {
      tooltips: {
        callbacks: {
          label: function(tooltipItem, data) {
            var label = data.datasets[tooltipItem.datasetIndex].label || "";

            if (label) {
              label += ": ";
            }
            label += Math.round(tooltipItem.yLabel * 100) / 100;
            return "hello";
          }
        }
      }
    }
  };
  return (
    <div>
      <Scatter data={popularPointData} options={options} />
    </div>
  );
}
