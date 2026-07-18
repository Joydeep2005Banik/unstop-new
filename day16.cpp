#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

static const int MAXN = 200005;
int n, q;
int a[MAXN];

ll sum[4 * MAXN];
int mx1[4 * MAXN], mx2[4 * MAXN], cnt1[4 * MAXN];

void pushup(int node) {
    int l = node * 2, r = node * 2 + 1;
    sum[node] = sum[l] + sum[r];
    if (mx1[l] == mx1[r]) {
        mx1[node] = mx1[l];
        cnt1[node] = cnt1[l] + cnt1[r];
        mx2[node] = max(mx2[l], mx2[r]);
    } else if (mx1[l] > mx1[r]) {
        mx1[node] = mx1[l];
        cnt1[node] = cnt1[l];
        mx2[node] = max(mx2[l], mx1[r]);
    } else {
        mx1[node] = mx1[r];
        cnt1[node] = cnt1[r];
        mx2[node] = max(mx1[l], mx2[r]);
    }
}

void applyTag(int node, int v) {
    if (v >= mx1[node]) return;
    sum[node] -= (ll)(mx1[node] - v) * cnt1[node];
    mx1[node] = v;
}

void pushdown(int node) {
    int l = node * 2, r = node * 2 + 1;
    applyTag(l, mx1[node]);
    applyTag(r, mx1[node]);
}

void build(int node, int l, int r) {
    if (l == r) {
        sum[node] = a[l];
        mx1[node] = a[l];
        mx2[node] = -1; 
        cnt1[node] = 1;
        return;
    }
    int mid = (l + r) / 2;
    build(node * 2, l, mid);
    build(node * 2 + 1, mid + 1, r);
    pushup(node);
}

void update(int node, int l, int r, int ql, int qr, int v) {
    if (qr < l || r < ql || mx1[node] <= v) return;
    if (ql <= l && r <= qr && mx2[node] < v) {
        applyTag(node, v);
        return;
    }
    pushdown(node);
    int mid = (l + r) / 2;
    update(node * 2, l, mid, ql, qr, v);
    update(node * 2 + 1, mid + 1, r, ql, qr, v);
    pushup(node);
}

ll query(int node, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return sum[node];
    pushdown(node);
    int mid = (l + r) / 2;
    return query(node * 2, l, mid, ql, qr) + query(node * 2 + 1, mid + 1, r, ql, qr);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    for (int i = 1; i <= n; i++) cin >> a[i];

    build(1, 1, n);

    string out;
    out.reserve(1 << 20);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r, v;
            cin >> l >> r >> v;
            update(1, 1, n, l, r, v);
        } else {
            int l, r;
            cin >> l >> r;
            ll res = query(1, 1, n, l, r);
            out += to_string(res);
            out += '\n';
        }
    }

    cout << out;
    return 0;
}