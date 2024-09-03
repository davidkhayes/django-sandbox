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

  const origin = window.location.origin;
  const url = `${origin}/testapp/status/${id}`;

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

  if (temp["status"] == "finished") {
    clearInterval(interval);
    return;
  }

  if (counter++ > 50) {
    spanId.innerText = "unknown"
    clearInterval(interval);
    return;
  }
};

window.onload = () => {
  spanId = document.getElementById("status");
  spanId.innerText = "started";
  interval = setInterval("getStatus(taskId)", 500);
}
