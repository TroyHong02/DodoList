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
  let [fetchList, setFetchList] = useState(false);

  let toggleNewListPopUp = () => {
    setShowNewListPopUp(!showNewListPopUp);
  };

  useEffect(() => {
    
    console.log("hi")
    fetch("http://localhost:5000/getlists", {})
      .then((res) => res.json())
      .then((resJSON) => setData(resJSON.data))
      .catch((error) => console.log(error));
  }, [fetchList]);

  let createNewList = (listName) => {
    //grab list name from html
    //send post request
    console.log(listName)
    fetch("http://localhost:5000/newlist", {
      method: "POST",
      headers: {
        "content-type": "application/json"
      },
      body: JSON.stringify({
        title: listName
      })
    }).then((res) => res.json())
      .then((resJSON) => setData(resJSON.data))
      //setFetchList => true
      .then(() => { 
        console.log("hello there")
        setFetchList(!fetchList)
      })
      .catch((error) => console.log(error));
  }

  return (
    <div>
      <Logo></Logo>
      <h1>AppPage</h1>
      <table>
        <thead>
          <tr>
            <th>List Name</th>
            <th># of Tasks</th>
          </tr>
        </thead>
        <tbody>
          {data && data.map(function(list){
            console.log(list)
            return <tr key={list["_id"]["$oid"] +"0"}>
              <td key={list["_id"]["$oid"] + "1"}><Link key={list["_id"]["$oid"] + "2"} to={"/app/" + list["_id"]}>{list["list_name"]}</Link></td>
              <td key={list["_id"]["$oid"] + "3"}>{list["tasks"].length}</td>
            </tr>;
          })}
        </tbody>
      </table>
      <button onClick={toggleNewListPopUp}>Create a New List</button>
      {showNewListPopUp && <NewListPopUp toggle={toggleNewListPopUp} createNewList={createNewList}/>}
    </div>
  );
}

export default AppPage;
