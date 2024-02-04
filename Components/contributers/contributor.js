const contributor = document.getElementById('contributor');

let allContributorsGithub = [];

let allContributorsAvatar = [];

function fetchAllContributors() {
    allContributorsGithub.forEach((githubLink, index) => {
        const contributorCard = document.createElement('div');
        contributorCard.classList.add('contributor-card');

        const avatar = document.createElement('img');
        avatar.src = allContributorsAvatar[index];

        const link = document.createElement('a');
        link.target = '_blank';
        link.href = githubLink;
        link.appendChild(avatar);

        contributorCard.appendChild(link);
        contributor.appendChild(contributorCard);
    });
}
fetchAllContributors();
