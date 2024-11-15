// Include Three.js or other 3D rendering libraries
import * as THREE from 'three';

function init() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Add Earth sphere
    const earthGeometry = new THREE.SphereGeometry(6371, 50, 50);
    const earthMaterial = new THREE.MeshBasicMaterial({ color: 0x0000ff, wireframe: true });
    const earth = new THREE.Mesh(earthGeometry, earthMaterial);
    scene.add(earth);

    // Add rocket
    const rocketGeometry = new THREE.CylinderGeometry(1, 1, 10, 32);
    const rocketMaterial = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const rocket = new THREE.Mesh(rocketGeometry, rocketMaterial);
    scene.add(rocket);

    // Camera and animation
    camera.position.z = 10000;

    const animate = function () {
        requestAnimationFrame(animate);
        rocket.position.y += 0.1;  // Move the rocket up
        renderer.render(scene, camera);
    };

    animate();
}

init();
