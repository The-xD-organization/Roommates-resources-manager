<template>
  <div id="app">
    <header>
      <div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="/">RoomMate Manager</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/">Start</b-nav-item>
        <b-nav-item-dropdown>
          <template v-slot:button-content>
            Rachunki
          </template>
          <b-dropdown-item href="#">Bierzące
          </b-dropdown-item>
          <b-dropdown-item href="#">Historia</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item href="/about">Obowiązki</b-nav-item>
        <b-nav-item href="#">To-Do</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Szukaj"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Szukaj</b-button>
        </b-nav-form>

        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <em>Konto</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
      <router-view/>
</div>
    </header>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
