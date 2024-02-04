const contributor = document.getElementById('contributor');

let allContributorsGithub = [];

let allContributorsAvatar = [];

function fetchAllContributors() {

    fetch('https://api.github.com/repos/Pankaj0038/dcodeKi/contributors')
        .then(response => response.json())
        .then(data => {

            data.forEach(contributor => {
                if (contributor.login !== 'Pankaj0038') {
                    allContributorsGithub.push(contributor.html_url);
                    allContributorsAvatar.push(contributor.avatar_url);
                }
            });

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
        })
}
fetchAllContributors();
