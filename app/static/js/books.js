const pages = document.querySelectorAll('.page');
let currentPage = 0;

function showPage(index) {
  pages[currentPage].style.display = 'none';
  pages[index].style.display = 'block';
  currentPage = index;
}

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
  } /* else if (currentPage === pages.length - 1) {
    currentPage = 0; 
    showPage(currentPage);
  } */
});
