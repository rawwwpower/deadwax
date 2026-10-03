# Genera el sample de audio de nana: "Dead Wax 2005", un loop original de ~24 s
# (bombo, caja, hi-hat, bajo y acordes de sinte). Todo sintetizado con stdlib,
# sin samples de terceros, así que no hay derechos de nadie metidos en el repo.
#   uso: python3 sintetizar.py && ffmpeg ... (ver hacer-media.sh)
import math, random, struct, wave, os

SR = 22050
BPM = 112
BEAT = 60 / BPM
BARS = 12
N = int(SR * BEAT * 4 * BARS)
buf = [0.0] * N
random.seed(2005)

def add(t0, samples, gain=1.0):
    i0 = int(t0 * SR)
    for k, s in enumerate(samples):
        if 0 <= i0 + k < N:
            buf[i0 + k] += s * gain

def kick():
    out = []
    for i in range(int(SR * 0.35)):
        t = i / SR
        f = 45 + 110 * math.exp(-t * 28)
        out.append(math.sin(2 * math.pi * f * t) * math.exp(-t * 9))
    return out

def snare():
    out = []
    for i in range(int(SR * 0.22)):
        t = i / SR
        out.append((random.uniform(-1, 1) * 0.8 + math.sin(2 * math.pi * 190 * t) * 0.4) * math.exp(-t * 18))
    return out

def hat(open_=False):
    out, prev = [], 0.0
    for i in range(int(SR * (0.18 if open_ else 0.05))):
        t = i / SR
        n = random.uniform(-1, 1)
        out.append((n - prev) * math.exp(-t * (14 if open_ else 70)))
        prev = n
    return out

def note(freq, dur, wave_='saw', a=0.01, r=0.15):
    out = []
    n = int(SR * dur)
    for i in range(n):
        t = i / SR
        env = min(1, t / a) * (1 if t < dur - r else max(0, (dur - t) / r))
        ph = (freq * t) % 1
        if wave_ == 'saw':
            s = 2 * ph - 1
        elif wave_ == 'square':
            s = 1 if ph < 0.5 else -1
        else:
            s = math.sin(2 * math.pi * ph)
        out.append(s * env)
    return out

def lowpass(x, k=0.08):
    y, acc = [], 0.0
    for s in x:
        acc += k * (s - acc)
        y.append(acc)
    return y

hz = lambda m: 440 * 2 ** ((m - 69) / 12)
# Am - F - C - G, lo más 2005 posible
prog = [(57, [69, 72, 76]), (53, [65, 69, 72]), (48, [64, 67, 72]), (55, [62, 67, 71])]
K, S, H, HO = kick(), snare(), hat(), hat(True)

for bar in range(BARS):
    t_bar = bar * 4 * BEAT
    root, chord = prog[bar % 4]
    full = bar >= 2
    for b in range(4):
        tb = t_bar + b * BEAT
        if full or b in (0, 2):
            add(tb, K, 0.9)
        if full and b in (1, 3):
            add(tb, S, 0.35)
        for h in range(2):
            add(tb + h * BEAT / 2, HO if (h == 1 and b == 3) else H, 0.12 if full else 0.07)
    if full and bar % 2 == 1:
        add(t_bar + 3.5 * BEAT, K, 0.6)
    # bajo en corcheas
    for e in range(8):
        m = root - 12 + (12 if e in (3, 6) else 0)
        add(t_bar + e * BEAT / 2, lowpass(note(hz(m), BEAT / 2 * 0.9, 'square', r=0.04), 0.12), 0.32)
    # acordes: pad de sierra filtrado
    if bar >= 4:
        for m in chord:
            add(t_bar, lowpass(note(hz(m), BEAT * 4, 'saw', a=0.25, r=0.6), 0.05), 0.11)
    # melodía arriba en los últimos compases
    if bar >= 8:
        mel = [chord[2] + 12, chord[1] + 12, chord[2] + 12, chord[0] + 12]
        for i, m in enumerate(mel):
            add(t_bar + i * BEAT, note(hz(m), BEAT * 0.8, 'sine', r=0.3), 0.13)

peak = max(abs(s) for s in buf) or 1
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dead-wax-2005.wav')
with wave.open(out, 'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(b''.join(struct.pack('<h', int(max(-1, min(1, s / peak * 0.9)) * 32767)) for s in buf))
print(out, round(N / SR, 1), 's')
