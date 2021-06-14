
import "../../Styles/main.css";
import Introduction from "../../Components/Introduction/Introduction";

function Home() {
  return (
    <div className="Home">
      <h1 className="headline">
        The Great Bot of MUACM
      </h1>
      <div className="LinksLayer">
        <a href="https://github.com/SuperbSaud/tgb-muacm">
          GitHub
        </a>
        •
        <a href="https://github.com/SuperbSaud/tgb-muacm/graphs/contributors">
          Contributors
        </a>
        •
        <a href="">
          Invite Bot to Discord Server
        </a>
        •
        <a href="http://medicaps.hosting.acm.org/">
          MUACM
        </a>
        •
        <a href="https://discord.gg/NHjFUKnwyx">
          MUACM Discord Community
        </a>
      </div>
      <Introduction />
    </div>
  )
}

export default Home;