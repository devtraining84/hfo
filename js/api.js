document.addEventListener("DOMContentLoaded", () => {
    alert("DOM ready!");

var form = document.getElementById("form");
    inputs = form.querySelectorAll("#form_step1");
    button = form.querySelector("#buttonstep1");

    span = form.querySelectorAll(".classspan" );

button.addEventListener("click", function (event) {
    arr=[];
    arr2=[];
    for (var i = 0, max = inputs.length; i < max; i += 1) {
   // Take only those inputs which are checkbox
   if (inputs[i].type === "checkbox" && inputs[i].checked) {
      arr.push(inputs[i].value);
      arr2.push(span[i].innerText);
   }
}

    console.log(arr);

    console.log(arr2);
});



  });

