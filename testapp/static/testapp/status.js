let spanId;     // element
let taskId;
let interval;
let counter = 0;

const handleError = (error) => {
  spanId.innerText = error;
  spanId.style.background = "lightgrey";
  spanId.style.color = "red";
  clearInterval(interval);
};

const getStatus = async (id) => {

  const origin = window.location.origin;
  const url = `${origin}/testapp/status/${id}`;

  let response, temp;

  if (!id) {
    handleError("error: no ID to check");
    return;
  }

  try {
    response = await fetch(url);
  } catch (error) {
    handleError(`error: ${error}`);
    return;
  }

  if (!response.ok) {
    handleError(`error (${response.status})`);
    return;
  }

  try {
    temp = await response.json();
  }
  catch (error) {
    handleError(error);
    return;
  }

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
  taskId = document.getElementById("task_id").innerHTML;
  interval = setInterval("getStatus(taskId)", 500);
}
