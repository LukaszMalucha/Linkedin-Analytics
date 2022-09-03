import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Sector from "./views/Sector.vue";
import Companies from "./views/Companies.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/sector/:category",
      name: "sector",
      component: Sector,
      props: true
    },
    {
      path: "/companies/:category",
      name: "companies",
      component: Companies,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
});
