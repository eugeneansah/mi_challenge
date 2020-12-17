import React, { useEffect,useState } from "react";
import { axios } from "./axios";
import ScatterChart from "./ScatterChart"; 

export default function Visualize() {
    const [visualise, setVisualise] = useState({});
 
  // let scatterData = {};
  function getVisualise() { 
    axios
      .get("/")
      .then(response => {
        if (response.data) {
          JSON.parse(response.data.most_popular_dropoff_points);
          // console.log(obj);
          setVisualise(response.data);
          // obj.features.forEach(feature => {
          //   data = {
          //     x: feature.geometry.coordinates[0],
          //     y: feature.geometry.coordinates[1]
          //   };
          //   dropOffData.push(data);
          // });
          // console.log(dropOffData);
          // console.log(obj.features[0].properties.name);
          // console.log(obj.features[0].geometry.coordinates);
          //   console.log(response.data.most_popular_dropoff_points.geometry);
        } 
      })
      .catch(err => console.log("Error", err));
    // console.log(response.data.most_popular_dropoff_points);
  }

  useEffect(() => {
    getVisualise();
  }, []);
  return (
    <div>
      <button onClick={getVisualise}>Simulate</button>
      <ScatterChart data={visualise} />
    </div>
  );
}
