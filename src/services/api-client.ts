import axios from "axios";

export default axios.create({
  baseURL: "https://api.rawg.io/api",
  params: {
    key: "eafe7147b6dc46f6bb8cd902225f688d",
  },
});
