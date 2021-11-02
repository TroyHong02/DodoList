import Logo from "../components/Logo";
import {Link} from "react-router-dom";
import styled from "styled-components";

const NavBarLink = styled(Link)`
    float: left;
    color: #f2f2f2;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
    font-size: 17px;
`;

const NavBarDiv = styled.div`
    background-color: rgb(13, 35, 122);
    overflow: hidden;
`;

function HomePage() {
  return (
    <NavBarDiv>
      <Logo></Logo>
      <h1>HomePage</h1>
      <NavBarLink to="/login">login</NavBarLink>
      <NavBarLink to="/signup">signup</NavBarLink>
    </NavBarDiv>
  );
}

export default HomePage;
