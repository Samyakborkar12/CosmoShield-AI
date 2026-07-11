const container = document.getElementById("earthContainer");

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
    45,
    container.clientWidth / container.clientHeight,
    0.1,
    1000
);

const renderer = new THREE.WebGLRenderer({
    antialias: true,
    alpha: true
});

renderer.setSize(
    container.clientWidth,
    container.clientHeight
);

container.innerHTML = "";
container.appendChild(renderer.domElement);

const geometry = new THREE.SphereGeometry(2, 64, 64);

const material = new THREE.MeshStandardMaterial({
    color: 0x2d8cff,
    roughness: 0.8,
    metalness: 0.1
});

const earth = new THREE.Mesh(
    geometry,
    material
);

scene.add(earth);

const light = new THREE.PointLight(
    0xffffff,
    3
);

light.position.set(5,3,5);

scene.add(light);

const ambient = new THREE.AmbientLight(
    0xffffff,
    1
);

scene.add(ambient);

camera.position.z = 5;

function animate(){

    requestAnimationFrame(animate);

    earth.rotation.y += 0.003;

    renderer.render(scene,camera);

}

animate();

window.addEventListener("resize",()=>{

    camera.aspect =
        container.clientWidth /
        container.clientHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(
        container.clientWidth,
        container.clientHeight
    );

});