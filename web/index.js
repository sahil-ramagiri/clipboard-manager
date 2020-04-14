fetch('../db.json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });
