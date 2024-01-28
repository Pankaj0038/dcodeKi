const contributor = document.getElementById('contributor');

let allContributorsGithub = ['https://github.com/daksh1210jain','https://github.com/basedBaba','https://github.com/k3s1','https://github.com/SGCODEX','https://github.com/amrikhore86',
'https://github.com/sukriti-kuila','https://github.com/jack-a129'];

let allContributorsAvatar = ['https://avatars.githubusercontent.com/u/137384322?s=64&v=4','https://avatars.githubusercontent.com/u/144726228?s=64&v=4','https://avatars.githubusercontent.com/u/123978864?s=64&v=4',
'https://avatars.githubusercontent.com/u/64886313?s=64&v=4','https://avatars.githubusercontent.com/u/73484308?s=64&v=4','https://avatars.githubusercontent.com/u/87015685?s=64&v=4',
'https://avatars.githubusercontent.com/u/113231783?s=64&v=4'];

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
