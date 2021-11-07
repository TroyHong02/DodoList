import Logo from "../components/Logo";
import {Link} from "react-router-dom";
import NewListPopUp from "../components/NewListPopUp";
import React, { useState, useEffect } from 'react';

// let getListsResponse = {
//   "success": true,
//   "data": [
//     {
//       "_id": "id",
//       "list_name": "dodo1",
//       "tasks": ["monkey", "derek", "robert", "troy"]
//     },
//     {
//       "_id": "id",
//       "list_name": "dodo2",
//       "tasks": ["monkey", "derek", "robert", "troy", "berty"]
//     },
//     {
//       "_id": "id",
//       "list_name": "dodo3",
//       "tasks": ["monkey", "derek", "robert", "troy", "derk", "toy"]
//     },
//   ],
// }

function AppPage() {

  let [showNewListPopUp, setShowNewListPopUp] = useState(false);
  let [data, setData] = useState([]);

  let toggleNewListPopUp = () => {
    setShowNewListPopUp(!showNewListPopUp);
  };

  useEffect(() => {
    console.log("hi")
    fetch("http://localhost:5000/getlists", {
      // mode: 'cors'
    }).then((res) => res.json())
      .then((resJSON) => setData(resJSON.data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <div>
      <Logo></Logo>
      <h1>AppPage</h1>
      <table>
        <tr>
          <th>List Name</th>
          <th># of Tasks</th>
        </tr>
        {data.map(function(list){
          return <tr>
            <td><Link to={"/app/" + list["_id"]}>{list["list_name"]}</Link></td>
            <td>{list["tasks"].length}</td>
          </tr>;
        })}
      </table>
      <button onClick={toggleNewListPopUp}>Create a New List</button>
      {showNewListPopUp ? <NewListPopUp toggle={toggleNewListPopUp} /> : null}
    </div>
  );
}

export default AppPage;
