import Logo from "../components/Logo";
import {Link} from "react-router-dom";

let getListsResponse = {
  "success": true,
  "data": [
    {
      "_id": "id",
      "list_name": "dodo1",
      "tasks": ["monkey", "derek", "robert", "troy"]
    },
    {
      "_id": "id",
      "list_name": "dodo2",
      "tasks": ["monkey", "derek", "robert", "troy", "berty"]
    },
    {
      "_id": "id",
      "list_name": "dodo3",
      "tasks": ["monkey", "derek", "robert", "troy", "derk", "toy"]
    },
  ],
}

function AppPage() {
  return (
    <div>
      <Logo></Logo>
      <h1>AppPage</h1>
      <table>
        <tr>
          <th>List Name</th>
          <th># of Tasks</th>
        </tr>
        {getListsResponse["data"].map(function(list){
          return <tr>
            <td><Link to={"/app/" + list["_id"]}>{list["list_name"]}</Link></td>
            <td>{list["tasks"].length}</td>
          </tr>;
        })}
      </table>
    </div>
  );
}

export default AppPage;
