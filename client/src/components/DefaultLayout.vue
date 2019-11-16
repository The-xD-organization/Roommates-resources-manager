<template>
    <div>
        <header>
            <b-navbar toggleable="lg" type="dark" variant="info">
                <b-navbar-brand href="/">RoomMate Manager</b-navbar-brand>

                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

                <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item href="/">Start</b-nav-item>
                    <b-nav-item-dropdown>
                    <template>
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
