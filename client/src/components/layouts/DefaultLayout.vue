<template>
    <div>
        <body>
            <section>
                <div class="wrapper">
        <header>
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand>
                    <router-link
                        class="navbar-brand"
                        to="/">
                            RoomMates Manager
                        </router-link>
                </b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item><router-link
                            class="nav-link"
                            to="/">
                                Start
                        </router-link></b-nav-item>
                         <b-nav-item><router-link
                            class="nav-link"
                            to="/bills">
                                Rachunki
                        </router-link></b-nav-item>
                    <b-nav-item><router-link
                            class="nav-link"
                            to="/tasks">
                                Obowiązki
                        </router-link></b-nav-item>
                        <b-nav-item disabled>
                        <router-link
                            class="nav-link"
                            to="/">
                                Długi
                        </router-link>
                    </b-nav-item>
                    <b-nav-item disabled>
                        <router-link
                            class="nav-link"
                            to="/">
                                Kalkulator
                        </router-link>
                    </b-nav-item>
                    <b-nav-item>
                        <router-link
                            class="nav-link"
                            to="/about">
                                About
                        </router-link>
                    </b-nav-item>
                </b-navbar-nav>

                <b-navbar-nav class="ml-auto">

                    <b-nav-item-dropdown right>
                    <template v-slot:button-content>
                        <em>Konto</em>
                    </template>
                    <b-dropdown-item href="#">Profile</b-dropdown-item>
                    <b-dropdown-item><router-link
                            class="link"
                            to="/logout">
                                Wyloguj
                        </router-link></b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </header>
        <main>
        <slot></slot>
        </main>

        <footer class="footer">
        <b-container fluid>
            <b-row class="text-center">
                <b-col>
                    <span class="text-white">Copyright © The "xD" organization</span>
                </b-col>
            </b-row>
        </b-container>
        </footer>
                </div>
            </section>
        </body>
    </div>
</template>

<script>
export default {
    name: 'DefaultLayout',
};
</script>

<style scoped>
body{
    padding: 0;
    margin: 0;
}
*{
    box-sizing: border-box;
}
section {
height: 100vh;
}
.wrapper {
min-height: 100%;
display: grid;
grid-template-rows: auto 1fr auto;
}
.footer{
  width: 100%;
  height: 60px;
  line-height: 60px;
  background-color: #17a2b8;
}

</style>
