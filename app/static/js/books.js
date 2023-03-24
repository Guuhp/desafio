const pages = document.querySelectorAll('.page');
let currentPage = 0;

function showPage(index) {
  pages[currentPage].style.display = 'none';
  pages[index].style.display = 'block';
  currentPage = index;
}

document.addEventListener('keydown', function (event) {
  if (event.keyCode === 37 && currentPage > 0) {
    showPage(currentPage - 1);
  } else if (event.keyCode === 39 && currentPage < pages.length - 1) {
    showPage(currentPage + 1);
  }
});

const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');

prevButton.addEventListener('click', function () {
  if (currentPage > 0) {
    showPage(currentPage - 1);
  }
});

nextButton.addEventListener('click', function () {
  if (currentPage < pages.length - 1) {
    showPage(currentPage + 1);
  }
})

