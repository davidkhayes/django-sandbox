let spanId;     // element
let taskId;     // set inline
let interval;
let counter = 0;

const getStatus = async (id) => {

  let response;

  if (id == null) {
    alert("no id to check. can't run.");
    clearInterval(interval);
    return;
  }
  
  const url = `http://localhost:8000/testapp/status/${id}`;

  try {
    response = await fetch(url);
  } catch (error) {
    alert(`error: ${error}`);
    clearInterval(interval);
    return;
  }

  const temp = await response.json();
  console.log(JSON.stringify(temp));
  
  spanId.innerText = temp["status"]

  if (temp["status"] == "finished") clearInterval(interval);
  if (counter++ > 30) clearInterval(interval);
};

window.onload = () => {
  spanId = document.getElementById("status");
  spanId.innerText = "started";
  interval = setInterval("getStatus(taskId)", 500);
}
