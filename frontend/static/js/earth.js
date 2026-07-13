/* ==========================================================
   COSMOSHIELD AI
   EARTH.JS
   PART 1
========================================================== */

const container = document.getElementById("earthContainer");

if (!container) {
    throw new Error("earthContainer not found");
}

/* ==========================================================
   SCENE
========================================================== */

const scene = new THREE.Scene();

/* ==========================================================
   CAMERA
========================================================== */

const camera = new THREE.PerspectiveCamera(

    45,

    container.clientWidth / container.clientHeight,

    0.1,

    1000

);

camera.position.set(0, 0, 3.8);

/* ==========================================================
   RENDERER
========================================================== */

const renderer = new THREE.WebGLRenderer({

    antialias: true,

    alpha: true

});

renderer.setPixelRatio(window.devicePixelRatio);

renderer.setSize(

    container.clientWidth,

    container.clientHeight

);

renderer.outputColorSpace = THREE.SRGBColorSpace;

renderer.shadowMap.enabled = true;

renderer.shadowMap.type = THREE.PCFSoftShadowMap;

container.innerHTML = "";

container.appendChild(renderer.domElement);

/* ==========================================================
   LIGHTS
========================================================== */

const ambientLight = new THREE.AmbientLight(

    0xffffff,

    1.3

);

scene.add(ambientLight);

const sunLight = new THREE.DirectionalLight(

    0xffffff,

    2.4

);

sunLight.position.set(

    5,

    2,

    5

);

sunLight.castShadow = true;

scene.add(sunLight);

/* ==========================================================
   TEXTURE LOADER
========================================================== */

const textureLoader = new THREE.TextureLoader();

/*
Use your local textures

earth_day.jpg
earth_night.jpg
earth_clouds.png (optional)

*/

const earthTexture = textureLoader.load(

    "/static/assets/textures/earth_day.jpg"

);

/* ==========================================================
   EARTH
========================================================== */

const earthGeometry = new THREE.SphereGeometry(

    1,

    128,

    128

);

const earthMaterial = new THREE.MeshStandardMaterial({

    map: earthTexture,

    roughness: 1,

    metalness: 0

});

const earth = new THREE.Mesh(

    earthGeometry,

    earthMaterial

);

earth.castShadow = true;

earth.receiveShadow = true;

scene.add(earth);
/* ==========================================================
   CLOUD LAYER
========================================================== */

const cloudsTexture = textureLoader.load(

    "/static/assets/textures/clouds.png"

);

const clouds = new THREE.Mesh(

    new THREE.SphereGeometry(1.015,128,128),

    new THREE.MeshStandardMaterial({

        map:cloudsTexture,

        transparent:true,

        opacity:.42,

        depthWrite:false

    })

);

scene.add(clouds);
/* ==========================================================
   SHOOTING STAR
========================================================== */

const shootingStar = new THREE.Mesh(

    new THREE.SphereGeometry(.025,16,16),

    new THREE.MeshBasicMaterial({

        color:0xffffff

    })

);

scene.add(shootingStar);

let shootingTimer = 0;
/* ==========================================================
   PART 2
   ATMOSPHERE
========================================================== */

const atmosphereGeometry = new THREE.SphereGeometry(

    1.04,

    128,

    128

);

const atmosphereMaterial = new THREE.MeshBasicMaterial({

    color: 0x4fc3ff,

    transparent: true,

    opacity: 0.18,

    side: THREE.BackSide

});

const atmosphere = new THREE.Mesh(

    atmosphereGeometry,

    atmosphereMaterial

);

scene.add(atmosphere);

/* ==========================================================
   STARS
========================================================== */

const starGeometry = new THREE.BufferGeometry();

const starVertices = [];

for(let i=0;i<4000;i++){

    starVertices.push(

        (Math.random()-0.5)*180,

        (Math.random()-0.5)*180,

        (Math.random()-0.5)*180

    );

}

starGeometry.setAttribute(

    "position",

    new THREE.Float32BufferAttribute(

        starVertices,

        3

    )

);

const starMaterial = new THREE.PointsMaterial({

    color:0xffffff,

    size:0.18,

    transparent:true,

    opacity:.9

});

const stars = new THREE.Points(

    starGeometry,

    starMaterial

);

scene.add(stars);

/* ==========================================================
   SUN
========================================================== */

const sun = new THREE.Mesh(

    new THREE.SphereGeometry(.22,32,32),

    new THREE.MeshBasicMaterial({

        color:0xffd54f

    })

);

sun.position.set(

    5,

    2,

    -4

);

scene.add(sun);

/* ---------- Glow ---------- */

const glow = new THREE.Sprite(

    new THREE.SpriteMaterial({

        color:0xffc107,

        transparent:true,

        opacity:.65

    })

);

glow.scale.set(

    2.8,

    2.8,

    2.8

);

glow.position.copy(

    sun.position

);

scene.add(glow);

/* ==========================================================
   MOON
========================================================== */

const moon = new THREE.Mesh(

    new THREE.SphereGeometry(.18,32,32),

    new THREE.MeshStandardMaterial({

        color:0xd9d9d9,

        roughness:1

    })

);

scene.add(moon);

/* ==========================================================
   SATELLITE
========================================================== */

const satelliteGroup = new THREE.Group();

scene.add(satelliteGroup);

/* Body */

const body = new THREE.Mesh(

    new THREE.BoxGeometry(

        .14,

        .14,

        .28

    ),

    new THREE.MeshStandardMaterial({

        color:0xd1d5db,

        metalness:.9,

        roughness:.3

    })

);

satelliteGroup.add(body);

/* Left Panel */

const panelMaterial = new THREE.MeshStandardMaterial({

    color:0x2563eb

});

const leftPanel = new THREE.Mesh(

    new THREE.BoxGeometry(

        .35,

        .02,

        .14

    ),

    panelMaterial

);

leftPanel.position.x = -.26;

satelliteGroup.add(leftPanel);

/* Right Panel */

const rightPanel = leftPanel.clone();

rightPanel.position.x = .26;

satelliteGroup.add(rightPanel);
/* ==========================================================
   ANIMATION
========================================================== */

const clock = new THREE.Clock();

function animate(){

    requestAnimationFrame(animate);

    const elapsed = clock.getElapsedTime();
    
    /* ==========================================================
   CLOUD ROTATION
========================================================== */

clouds.rotation.y += 0.0025;
    /* ==========================================================
   STAR TWINKLE
========================================================== */

starMaterial.opacity =

0.75 +

Math.sin(elapsed*2)*0.2;

    /* ==========================================================
   MOUSE CONTROL
========================================================== */

let mouseX = 0;

let mouseY = 0;

document.addEventListener("mousemove",(event)=>{

    mouseX =

        (event.clientX / window.innerWidth - 0.5) * 0.3;

    mouseY =

        (event.clientY / window.innerHeight - 0.5) * 0.2;

});
    /* ----------------------------
       EARTH ROTATION
    ----------------------------- */

    earth.rotation.y += 0.0018;

    atmosphere.rotation.y += 0.0022;
    earth.rotation.y +=

    (mouseX - earth.rotation.y) * 0.02;

earth.rotation.x +=

    (mouseY - earth.rotation.x) * 0.02;

    /* ----------------------------
       STAR FIELD
    ----------------------------- */

    stars.rotation.y += 0.00008;

    /* ----------------------------
       MOON ORBIT
    ----------------------------- */

    moon.position.x = Math.cos(elapsed * 0.35) * 3;

    moon.position.z = Math.sin(elapsed * 0.35) * 3;

    moon.position.y = 0.45;

    /* ----------------------------
       SATELLITE ORBIT
    ----------------------------- */

    satelliteGroup.position.x = Math.cos(elapsed) * 1.7;

    satelliteGroup.position.z = Math.sin(elapsed) * 1.7;

    satelliteGroup.position.y =

        Math.sin(elapsed * 2) * 0.25;

    satelliteGroup.lookAt(earth.position);

    /* ----------------------------
       SUN PULSE
    ----------------------------- */

    const pulse =

        1 + Math.sin(elapsed * 2) * 0.08;

    glow.scale.set(

        2.8 * pulse,

        2.8 * pulse,

        2.8 * pulse

    );

    renderer.render(scene,camera);

}

animate();

/* ==========================================================
   SHOOTING STAR
========================================================== */

shootingTimer += 0.02;

if(shootingTimer>12){

    shootingTimer=0;

}

shootingStar.position.x=

4-shootingTimer;

shootingStar.position.y=

2.2-shootingTimer*0.25;

shootingStar.position.z=-2;

/* ==========================================================
   RESPONSIVE
========================================================== */

window.addEventListener(

    "resize",

    ()=>{

        camera.aspect =

            container.clientWidth /

            container.clientHeight;

        camera.updateProjectionMatrix();

        renderer.setSize(

            container.clientWidth,

            container.clientHeight

        );

    }

);
/* ==========================================================
   CAMERA FLOAT
========================================================== */

camera.position.y=

Math.sin(elapsed*.5)*0.06;

camera.lookAt(

earth.position
);