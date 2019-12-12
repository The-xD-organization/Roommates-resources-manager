<template>
    <div>
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
                    <b-nav-item-dropdown text="Rachunki" right class="py-2">
                    <b-dropdown-item><router-link
                            class="link"
                            to="/bills">
                                Bieżące
                        </router-link></b-dropdown-item>
                    <b-dropdown-item>Historia</b-dropdown-item>
                    </b-nav-item-dropdown>
                    <b-nav-item><router-link
                            class="nav-link"
                            to="/tasks">
                                Obowiązki
                        </router-link></b-nav-item>
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

        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'DefaultLayout',
};
</script>

<style scoped>

</style>
