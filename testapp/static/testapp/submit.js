const doSubmit = () => {
  const numberId = document.getElementById("number");

  // there are counts in both forms.
  const counts = document.getElementsByClassName("count");
  for (let i=0; i < counts.length; i++) {
    counts[i].value = numberId.value;
  }
}
