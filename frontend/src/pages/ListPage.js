import Logo from "../components/Logo";

let getTasksResponse = {
    'success': true,
    'data': [
        {
            "_id": "id",
            "task_name": "wash dishes",
            "task_desc": "wash the dishes",
            "inserted_time": "03/20/2021",
            "due_date": "04/20/2021",
            "status": "incomplete"
        },
        {
            "_id": "id",
            "task_name": "walk the dog",
            "task_desc": "walk derek",
            "inserted_time": "03/20/2021",
            "due_date": "04/20/2021",
            "status": "incomplete"
        },
        {
            "_id": "id",
            "task_name": "feed the cat",
            "task_desc": "feed derek jr.",
            "inserted_time": "03/20/2021",
            "due_date": "04/20/2021",
            "status": "incomplete"
        }
    ]
}

function ListPage() {
    return (
        <div> 
            <Logo></Logo>
            <h1>My List</h1>
            <table>
                <tr>
                <th>Task</th>
                <th>Desc</th>
                <th>Created On</th>
                <th>Due by</th>
                <th>Status</th>
                </tr>
                {getTasksResponse["data"].map(function(task){
                return <tr>
                    <td>{task["task_name"]}</td>
                    <td>{task["task_desc"]}</td>
                    <td>{task["inserted_time"]}</td>
                    <td>{task["due_date"]}</td>
                    <td>{task["status"]}</td>
                </tr>;
                })}
            </table>

        </div>
    )
}

export default ListPage;